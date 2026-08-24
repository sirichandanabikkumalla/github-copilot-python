#!/usr/bin/env python
"""Quick test to verify the Check Solution enhancements."""
import copy
import sys
from starter.app import app as sudoku_app
from starter.app import CURRENT

def test_implementation():
    """Test the enhanced check solution feature."""
    sudoku_app.testing = True
    client = sudoku_app.test_client()
    
    print("=" * 60)
    print("Testing Enhanced Check Solution Feature")
    print("=" * 60)
    
    # Test 1: New game
    print("\n[Test 1] Creating a new game...")
    response = client.get('/new?clues=25')
    assert response.status_code == 200
    data = response.get_json()
    assert 'puzzle' in data
    assert CURRENT['solution'] is not None
    print("✓ New game created successfully")
    
    # Test 2: Check complete correct solution
    print("\n[Test 2] Checking complete correct solution...")
    solution = CURRENT['solution']
    response = client.post('/check', json={'board': solution})
    data = response.get_json()
    assert response.status_code == 200
    assert data['incorrect'] == []
    assert data['complete'] is True
    assert data['solved'] is True
    print("✓ Complete correct solution detected: 'solved' = True")
    
    # Test 3: Check incomplete board
    print("\n[Test 3] Checking incomplete board (with empty cells)...")
    incomplete_board = copy.deepcopy(solution)
    incomplete_board[0][0] = 0  # Empty a cell
    incomplete_board[5][5] = 0  # Empty another cell
    response = client.post('/check', json={'board': incomplete_board})
    data = response.get_json()
    assert response.status_code == 200
    assert data['complete'] is False
    assert data['solved'] is False
    print("✓ Incomplete board detected: 'complete' = False")
    
    # Test 4: Check complete board with incorrect cells
    print("\n[Test 4] Checking complete board with incorrect cells...")
    incorrect_board = copy.deepcopy(solution)
    original_value = incorrect_board[0][0]
    incorrect_board[0][0] = (original_value % 9) + 1  # Change a value
    response = client.post('/check', json={'board': incorrect_board})
    data = response.get_json()
    assert response.status_code == 200
    assert len(data['incorrect']) > 0  # Should report the incorrect cell
    assert data['complete'] is True
    assert data['solved'] is False
    print(f"✓ Incorrect cells detected: 'solved' = False, incorrect cells = {data['incorrect']}")
    
    # Test 5: Check incomplete board with incorrect values
    print("\n[Test 5] Checking incomplete board with some incorrect cells...")
    mixed_board = copy.deepcopy(solution)
    mixed_board[0][0] = 0  # Empty a cell
    mixed_board[1][1] = (mixed_board[1][1] % 9) + 1  # Make a cell incorrect
    response = client.post('/check', json={'board': mixed_board})
    data = response.get_json()
    assert response.status_code == 200
    assert data['complete'] is False
    assert data['solved'] is False
    print("✓ Mixed board (incomplete and incorrect) handled correctly")
    
    print("\n" + "=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)
    print("\nImplementation Summary:")
    print("- Backend returns: 'incorrect', 'complete', 'solved'")
    print("- Frontend detects 3 scenarios:")
    print("  1. Incomplete: Shows 'Please fill all empty cells'")
    print("  2. Solved: Shows 'Congratulations! You solved it!'")
    print("  3. Incorrect: Shows 'Some cells are incorrect' + highlights")
    print("- Locked/prefilled cells are never highlighted")
    print("- Correct entries remain unchanged visually")

if __name__ == '__main__':
    try:
        test_implementation()
        sys.exit(0)
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
