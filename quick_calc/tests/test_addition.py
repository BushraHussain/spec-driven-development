import pytest
import sys
import os
# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.quick_calc import add


class TestAddition:
    """Test cases for the add function covering all edge cases."""
    
    def test_positive_integers(self):
        """Test addition of positive integers."""
        assert add(2, 3) == 5
        assert add(100, 200) == 300
        assert add(1, 1) == 2
    
    def test_negative_integers(self):
        """Test addition of negative integers."""
        assert add(-2, -3) == -5
        assert add(-100, -200) == -300
        assert add(-1, -1) == -2
    
    def test_mixed_positive_negative_integers(self):
        """Test addition of positive and negative integers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
        assert add(10, -10) == 0
        assert add(-10, 10) == 0
    
    def test_zero_addition(self):
        """Test addition involving zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(-5, 0) == -5
        assert add(0, -5) == -5
    
    def test_positive_floats(self):
        """Test addition of positive floating point numbers."""
        assert abs(add(2.5, 3.7) - 6.2) < 1e-10  # Using approximate comparison
        assert add(1.1, 2.2) == pytest.approx(3.3)
    
    def test_negative_floats(self):
        """Test addition of negative floating point numbers."""
        assert add(-2.5, -3.7) == pytest.approx(-6.2)
        assert add(-1.1, -2.2) == pytest.approx(-3.3)
    
    def test_mixed_positive_negative_floats(self):
        """Test addition of positive and negative floating point numbers."""
        assert add(5.5, -3.3) == pytest.approx(2.2)
        assert add(-5.5, 3.3) == pytest.approx(-2.2)
        assert add(10.0, -10.0) == 0.0
    
    def test_integer_and_float(self):
        """Test addition of integers and floats."""
        assert add(5, 2.5) == 7.5
        assert add(2.5, 5) == 7.5
        assert add(-5, 2.5) == -2.5
        assert add(2.5, -5) == -2.5
    
    def test_large_numbers(self):
        """Test addition of large numbers."""
        assert add(1000000, 2000000) == 3000000
        assert add(1e10, 1e10) == 2e10
        assert add(-1e10, 1e10) == 0
    
    def test_very_small_numbers(self):
        """Test addition of very small numbers."""
        assert add(1e-10, 1e-10) == pytest.approx(2e-10)
        assert add(1e-15, 0) == pytest.approx(1e-15)
    
    def test_floating_point_precision(self):
        """Test addition with floating point precision considerations."""
        assert add(0.1, 0.2) == pytest.approx(0.3)
    
    def test_type_error_with_strings(self):
        """Test that adding strings raises TypeError."""
        with pytest.raises(TypeError):
            add("hello", "world")
        with pytest.raises(TypeError):
            add("5", 3)
        with pytest.raises(TypeError):
            add(5, "3")
    
    def test_type_error_with_lists(self):
        """Test that adding lists raises TypeError."""
        with pytest.raises(TypeError):
            add([1, 2], [3, 4])
        with pytest.raises(TypeError):
            add([1], 5)
        with pytest.raises(TypeError):
            add(5, [1])
    
    def test_type_error_with_none(self):
        """Test that adding None raises TypeError."""
        with pytest.raises(TypeError):
            add(None, 5)
        with pytest.raises(TypeError):
            add(5, None)
        with pytest.raises(TypeError):
            add(None, None)
    
    def test_type_error_with_boolean(self):
        """Test that adding booleans raises TypeError."""
        with pytest.raises(TypeError):
            add(True, 5)
        with pytest.raises(TypeError):
            add(5, False)
        with pytest.raises(TypeError):
            add(True, False)
    
    def test_type_error_with_dict(self):
        """Test that adding dicts raises TypeError."""
        with pytest.raises(TypeError):
            add({}, {})
        with pytest.raises(TypeError):
            add({"a": 1}, 5)
        with pytest.raises(TypeError):
            add(5, {"a": 1})
    
    def test_type_error_with_set(self):
        """Test that adding sets raises TypeError."""
        with pytest.raises(TypeError):
            add({1, 2}, {3, 4})
        with pytest.raises(TypeError):
            add({1, 2}, 5)
        with pytest.raises(TypeError):
            add(5, {1, 2})