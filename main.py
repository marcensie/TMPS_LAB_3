from workerdb import Workerdb
from paysystem import PaySystem
from performancereview import PerformanceReviewSystem
from administratorbuilder import AdministratorBuilder
from decorators.performancedecorator import PerformanceReviewDecorator
from models.doctor import Doctor
from workermanagesys import WorkerManagementSystem

def main():

    workers = []
    workers.append(Doctor(1, "worker1", 15000))
    workers.append(Doctor(2, "worker2", 15000))
    workers.append(AdministratorBuilder().set_name("administrator1").set_salary(18000).build())

    db = Workerdb()
    for worker in workers:
        db.add_Worker(worker)

    reviews = []
    reviews.append(PerformanceReviewDecorator(workers[0], "number one"))
    reviews.append(PerformanceReviewDecorator(workers[1], "number two"))
    reviews.append(PerformanceReviewDecorator(workers[2], "number three"))

    review_system = PerformanceReviewSystem()
    for review in reviews:
        review_system.add_performance_review(review, review.get_performance_review())

    wms = WorkerManagementSystem(db, PaySystem(), review_system)
    Workers = wms.get_Workers()

    print("All Workers:")
    for Worker in Workers:
        print("Name: {}, Salary: {}".format(Worker.get_name(), Worker.get_salary()))

    wms.raise_salary(workers[0], 1300)

if __name__ == "__main__":
    main()
