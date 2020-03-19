import pytest

def capitalize_case(word, str) :
    if not isinstance(word, str) :
      raise TypeError('Type provide is not a string! The allowed type is a string')
    return x.capitalize()
    
def test_capital_case():
  assert capital_case('semaphore') == 'Semaphore'
  
def test_raises_expression_on_non_string_argument():
  with pytest.raises(TypeError):
    capital_case(9)
