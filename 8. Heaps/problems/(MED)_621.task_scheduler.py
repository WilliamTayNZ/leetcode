import heapq
# The legendary 3500 ms solution, left untouched

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_counter = Counter(tasks) # O(tasks)

        # We don't care about the task identifiers, just the frequencies
        max_heap = [freq for freq in freq_counter.values()]
        heapq.heapify_max(max_heap)

        time = 0

        while max_heap: 
            cycle = n + 1 # cooling interval + 1 (for the current task)

            frequencies_to_restore = [] # store frequencies of tasks to be restored after decrementing

            task_count = 0

            while cycle > 0 and max_heap:
                cycle -= 1
                freq = heapq.heappop_max(max_heap)
                if freq > 1:
                    freq -= 1
                    frequencies_to_restore.append(freq)
                task_count += 1
            
            for popped_freq in frequencies_to_restore:
                heapq.heappush_max(max_heap, popped_freq)

            if max_heap:
                time += n + 1
            else:
                time += task_count

        return time


class LegendarySolution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Interval can do nothing
        # Or complete 1 task
        # Must be at least n intervals between 2 tasks of same label

        # Min number of CPU intervals to complete all task

        # 0 <= n <= 100

        # 1. Use a loop to create a dict label : cooldown and a dict label : frequency (O(n))

        label_to_cooldown = {}
        label_to_frequency = {}

        for task in tasks:
            label_to_frequency[task] = label_to_frequency.get(task, 0) + 1

        for label in label_to_frequency:
            label_to_cooldown[label] = 0


        # 2. Create max-heap [frequency, label] (O(n))

        labels_heap = []

        for label, frequency in label_to_frequency.items():
            labels_heap.append([frequency, label])

        heapq.heapify_max(labels_heap)

        # 3. Iterate

        num_intervals = 0

        while labels_heap:
            # print(f"Label to cooldown: {label_to_cooldown}")
            # print(f"Labels_heap [frequency, label]: {labels_heap}")
            # print()

            num_intervals += 1
            push_back_later = []

            popped = heapq.heappop_max(labels_heap)

        # While popped labels have cooldown greater than 0, pop and queue them label to be pushed back in later. Then check the next label
            while labels_heap and label_to_cooldown[popped[1]] > 0:
                push_back_later.append(popped)
                popped = heapq.heappop_max(labels_heap)

            # if popped label's cooldown is 0, reduce the frequency by 1 and reset the cooldown to n
            # This represents a task being done
            if label_to_cooldown[popped[1]] == 0:
                label_to_cooldown[popped[1]] = n + 1
                popped[0] -= 1

                if popped[0] > 0: # If the label's frequency still over 0
                    push_back_later.append(popped) # Push the label back
                    # Else, the label won't be pushed back

            else:
                push_back_later.append(popped) # If the cooldown isn't 0, we still have to push it back

            # If we popped all labels and all cooldowns above 0, do nothing

            # Reduce cooldown for each label
            for label in label_to_cooldown:
                if label_to_cooldown[label] > 0:
                    label_to_cooldown[label] -= 1

            for frequency_and_label in push_back_later:
                heapq.heappush_max(labels_heap, frequency_and_label)

        return num_intervals
            
            
        

                

        


       
        # so once something has been proeprly popped, push back all the other labels

        # All the while, we increment the number of intervals

        # When heap is empty, return number of intervals