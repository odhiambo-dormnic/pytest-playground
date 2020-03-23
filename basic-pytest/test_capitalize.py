import pytest

def capital_case(x):
    if not isinstance(x, str):
	    raise TypeError('You have not provided a string!')
    return x.capitalize()

def test_capital_case():
   assert capital_case('semaphore') == 'Semaphore'

def test_raises_expression_on_non_string_argument():
    with pytest.raises(TypeError):
	    capital_case(9)			 
	
