import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізуємо купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Повторюємо, поки в купі залишається більше одного кабелю
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі з купи
        first_shortest = heapq.heappop(cables)
        second_shortest = heapq.heappop(cables)
        
        # Об'єднуємо ці два кабелі
        combined_length = first_shortest + second_shortest
        
        # Додаємо отриманий кабель знову до купи
        heapq.heappush(cables, combined_length)
        
        # Додаємо вартість цього з'єднання до загальних витрат
        total_cost += combined_length

        # Друк проміжних результатів
        print(
            f"Об'єднання кабелів {first_shortest} та {second_shortest} з витратами {combined_length}. Загальні витрати: {total_cost}"
        )
        print(f"Поточний стан купи: {cables}")
    
    return total_cost

if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
