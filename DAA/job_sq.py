
class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


def job_sequencing(jobs, max_deadline):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    result = [-1] * max_deadline
    total_profit = 0

    for job in jobs:
        for slot in range(min(max_deadline, job.deadline)-1, -1, -1):
            if result[slot] == -1:
                result[slot] = job.id
                total_profit += job.profit
                break

    print("Selected jobs (in slot order) :", [
          job_id for job_id in result if job_id != -1])
    return total_profit


def main():
    jobs = [
        Job('J1', 2, 100),
        Job('J2', 1, 19),
        Job('J3', 2, 27),
        Job('J4', 1, 25),
        Job('J5', 3, 15),
    ]

    max_deadline = max(job.deadline for job in jobs)

    max_profit = job_sequencing(jobs, max_deadline)

    print(f"Total Profit : {max_profit}")


if __name__ == '__main__': 
    main()