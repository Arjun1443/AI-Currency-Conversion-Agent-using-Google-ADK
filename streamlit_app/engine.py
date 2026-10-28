from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def convert(amount,rate,fee):
    amount,rate,fee=map(lambda x:Decimal(str(x)),(amount,rate,fee))
    if not all(x.is_finite() for x in [amount,rate,fee]) or amount<0 or rate<=0 or fee<0 or fee>100:
        raise ValueError('Use a nonnegative amount, a positive rate, and a fee between 0 and 100.')
    gross=amount*rate
    deduction=gross*fee/Decimal(100)
    quantize=lambda x: x.quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
    return {'gross':quantize(gross),'fee':quantize(deduction),'net':quantize(gross-deduction)}
