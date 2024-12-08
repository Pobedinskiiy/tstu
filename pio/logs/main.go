package main

import (
	"fmt"
	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
	"github.com/spf13/viper"
	"log"
	"math/rand"
	"strings"
	"time"
)

type Config struct {
	Host     string
	Port     string
	Username string
	Password string
	DBName   string
	SSLMode  string
}

func initConfig() error {
	viper.AddConfigPath("configs")
	viper.SetConfigName("config")
	return viper.ReadInConfig()
}

var userTypes = [...]string{
	"Новые пользователи",
	"Регулярные посетители",
	"Подписчики на новости",
	"Покупатели товаров",
	"Потенциальные клиенты",
	"Пользователи мобильных устройств",
	"Пользователи с высокой вовлечённостью",
	"Гости с поисковых систем",
	"Пользователи, пришедшие по ссылкам",
	"Посетители из социальных сетей",
}

func NewPostgresBD(conf Config) (*sqlx.DB, error) {
	db, err := sqlx.Open("postgres",
		fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=%s",
			conf.Host, conf.Port, conf.Username, conf.Password, conf.DBName, conf.SSLMode))
	if err != nil {
		return nil, err
	}

	err = db.Ping()
	if err != nil {
		return nil, err
	}

	return db, nil
}

func AddedEntries(db *sqlx.DB, n int) {
	log.Printf("Let's start adding records to the table")
	rand.Seed(time.Now().UnixNano())
	lastPercent := -1
	countPercent := 0
	start := time.Now()

	numCol := 4
	batchSize := n / 100
	if batchSize*numCol > 65535 {
		batchSize = 65535 / numCol
	}
	records := make([]interface{}, 0, batchSize*numCol)

	tx, err := db.Beginx()
	if err != nil {
		log.Fatalf("Failed to start transaction: %v", err)
		return
	}
	defer func(tx *sqlx.Tx) {
		err := tx.Rollback()
		if err != nil {

		}
	}(tx)

	randomVisitDate := 365 * 24 * 60 * 60

	for i := 0; i < n; i++ {
		percentage := (i + 1) * 100 / n
		if percentage%10 == 0 && percentage != lastPercent {
			log.Printf("%d%% added entries", percentage)
			lastPercent = percentage
			countPercent++
		}
		userType := userTypes[rand.Intn(len(userTypes))]
		pageID := rand.Intn(500) + 1
		duration := rand.Intn(501) + 100
		visitDate := time.Now().AddDate(-rand.Intn(3), 0, 0).Add(time.Duration(rand.Intn(randomVisitDate)) * time.Second)

		records = append(records, userType, pageID, duration, visitDate)

		if len(records) == batchSize*numCol {
			query := `INSERT INTO logs (user_type, page_id, duration, visit_date) VALUES `
			valuePlaceholders := make([]string, 0, batchSize)

			for j := 0; j < batchSize*numCol; j += numCol {
				valuePlaceholders = append(valuePlaceholders, fmt.Sprintf("($%d, $%d, $%d, $%d)", j+1, j+2, j+3, j+4))
			}

			query += strings.Join(valuePlaceholders, ", ")

			_, err := tx.Exec(query, records...)
			if err != nil {
				log.Fatalf("Failed to insert logs: %v", err)
				return
			}

			records = records[:0]
		}
	}

	if len(records) > 0 {
		query := `INSERT INTO logs (user_type, page_id, duration, visit_date) VALUES `
		valuePlaceholders := make([]string, 0, len(records)/numCol)

		for j := 0; j < len(records); j += numCol {
			valuePlaceholders = append(valuePlaceholders, fmt.Sprintf("($%d, $%d, $%d, $%d)", j+1, j+2, j+3, j+4))
		}

		query += strings.Join(valuePlaceholders, ", ")

		_, err := tx.Exec(query, records...)
		if err != nil {
			log.Fatalf("Failed to insert logs: %v", err)
			return
		}
	}

	if countPercent < 11 {
		log.Printf("100%% added entries")
	}

	if err := tx.Commit(); err != nil {
		log.Fatalf("Failed to commit transaction: %v", err)
		return
	}

	log.Printf("Entries added successfully, lead time: %v", time.Since(start))
}

func main() {
	if err := initConfig(); err != nil {
		log.Fatalf("Failed to init configs: %v", err)
	}

	db, err := NewPostgresBD(Config{
		Host:     viper.GetString("host"),
		Port:     viper.GetString("port"),
		Username: viper.GetString("user_name"),
		Password: viper.GetString("password"),
		DBName:   viper.GetString("bd_name"),
		SSLMode:  viper.GetString("ssl_mode"),
	})
	if err != nil {
		log.Fatalf("Failed to init db connection, error: %s", err)
	}

	AddedEntries(db, 7000000)
}
