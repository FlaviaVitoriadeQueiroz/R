#1
import pandas as pd

# Dados
poker_vector = [140, -50, 20, -120, 240]
roulette_vector = [-24, -50, 100, -350, 10]
days_vector = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Criando DataFrame
df = pd.DataFrame({
    "Poker": poker_vector,
    "Roulette": roulette_vector
}, index=days_vector)

print(df)

# Em r
poker_vector <- c(140, -50, 20, -120, 240)

roulette_vector <-  c(-24, -50, 100, -350, 10)

days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

names(poker_vector) <-   days_vector
names(roulette_vector) <- days_vector



#2
# Total winnings with poker
total_poker = sum(poker_vector)

# Total winnings with roulette
total_roulette = sum(roulette_vector)

# Total winnings overall
total_week = total_poker + total_roulette

print(total_poker)
print(total_roulette)
print(total_week)

# Em r
# Total winnings with poker
total_poker <- sum(poker_vector)

# Total winnings with roulette
total_roulette <-  sum(roulette_vector)

# Total winnings overall
total_week <- total_poker + total_roulette

total_week


#3 Lista
# Python + NumPy x[[1,4]]

# em r x[c(1,4)]