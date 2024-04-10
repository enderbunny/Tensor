
function task21(arr) {
    var step1 = arr.reduce(function(arr1, item) {
        var year = item.year;
        var month = item.month;

        if (!arr1.some(el => el.year == year && el.month == month)) {
            arr1.push({
                year: year, month: month, opsCount: 0
            })
        }
        arr1[arr1.findIndex(el => el.year == year && el.month == month)].opsCount ++;

        return arr1;
    }, []);

    step1.sort((a, b) => b.opsCount - a.opsCount);

    return step1.slice(0,3);
}

function task22(year, month, arr) {
    var arr1 = arr.filter(function(item) {
        return item.year == year && item.month == month;
    });

    var monthRefill = 0;
    var monthWithdrawal = 0;
    var rank = "Бронзовый";

    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i].type == 'replenishment') {
            monthRefill += arr1[i].amount;
        }
        else {
            monthWithdrawal += arr1[i].amount;
        }
    }

    var withdrawalRate = monthWithdrawal / monthRefill;
    if (withdrawalRate < 0.15){
        rank = "Золотой"
    }else if (withdrawalRate < 0.3) {
        rank = "Серебряный"
    }

    return {
        monthBalance: monthRefill - monthWithdrawal,
        monthWithdrawal: monthWithdrawal,
        withdrawalRate: Math.round(withdrawalRate * 10000) / 10000,
        rank: rank
    };
}

function task23(arr) {
    return arr;
}