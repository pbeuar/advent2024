
reports = []

with open('input') as f:
    for line in f:
        reports.append([int(x) for x in line.strip().split()])


def gap(report):
    if 0 in report:
        return False
    report_plus = [abs(x) for x in report]
    return min(report_plus) >= 1 and max(report_plus) <= 3


def all_increasing_or_decreasing(report):
    first = report[0] > 0
    for dif in report[1:]:
        if not (dif > 0) == first:
            return False
    return True


def check_report(report):
    diff = [report[x]-report[x+1] for x in range(len(report)-1)]
    return gap(diff) and all_increasing_or_decreasing(diff)


good_reports = []
ok_reports = []

for report in reports:
    if check_report(report):
        good_reports.append(report)

    else:
        for i in range(len(report)):
            temp_report = report.copy()
            del temp_report[i]
            if check_report(temp_report):
                ok_reports.append([report, i])
                break
            
answer1 = len(good_reports)
# 624

answer2 = answer1 + len(ok_reports)
# 658


    