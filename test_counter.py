import time
from altunityrunner import AltrunUnityDriver, AltUnityAndroid, AltUnityIos, AltUnityPortForwarding

class TestCounterApp:
    
    def __init__(self):
        self.altdriver = None
        
    def setup(self):
        """Initialize connection to Unity application"""
        print("Connecting to Unity application...")
        try:
            self.altdriver = AltrunUnityDriver()
            print("Successfully connected to Unity application")
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
    
    def teardown(self):
        """Clean up after tests"""
        if self.altdriver:
            self.altdriver.stop()
            print("Connection closed")
    
    def test_button_interactable(self):
        """Test that the count button is interactable"""
        print("\n1. Testing button interactability...")
        try:
            submit_button = self.altdriver.find_object("SubmitButton")
            if submit_button and submit_button.enabled:
                print("Button is interactable")
                return True
            else:
                print("Button is NOT interactable")
                return False
        except Exception as e:
            print(f"Error testing button interactability: {e}")
            return False
    
    def test_counter_increases(self):
        """Test that counter increases when button is pressed"""
        print("\n2. Testing counter increment...")
        try:
            # Get initial counter value
            counter_text = self.altdriver.find_object("CounterText")
            initial_count = int(counter_text.get_text())
            print(f"Initial count: {initial_count}")
            
            # Click the button
            submit_button = self.altdriver.find_object("SubmitButton")
            submit_button.tap()
            time.sleep(1)  # Wait for update
            
            # Get new counter value
            new_count = int(counter_text.get_text())
            print(f"Count after click: {new_count}")
            
            if new_count == initial_count + 1:
                print("Counter increases correctly")
                return True
            else:
                print("Counter did NOT increase")
                return False
                
        except Exception as e:
            print(f"Error testing counter increment: {e}")
            return False
    
    def test_counter_stops_at_ten(self):
        """Test that counter stops at exactly 10 after 10 presses"""
        print("\n3. Testing counter stops at 10...")
        try:
            # Reset counter if needed
            counter_text = self.altdriver.find_object("CounterText")
            submit_button = self.altdriver.find_object("SubmitButton")
            
            # Click 10 times
            for i in range(10):
                submit_button.tap()
                time.sleep(0.5)
            
            # Get final count
            final_count = int(counter_text.get_text())
            print(f"Final count after 10 clicks: {final_count}")
            
            if final_count == 10:
                print("Counter stops at 10 correctly")
                return True
            else:
                print(f"Counter should be 10, but got {final_count}")
                return False
                
        except Exception as e:
            print(f"Error testing counter limit: {e}")
            return False

def main():
    """Main test execution"""
    print("Starting QA Engineer Test Suite")
    print("=" * 50)
    
    test_suite = TestCounterApp()
    
    if not test_suite.setup():
        print("Cannot proceed without connection")
        return
    
    results = []
    
    # Run all tests
    results.append(test_suite.test_button_interactable())
    results.append(test_suite.test_counter_increases())
    results.append(test_suite.test_counter_stops_at_ten())
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY:")
    print(f"Tests passed: {sum(results)}/{len(results)}")
    
    if all(results):
        print("All tests passed!")
    else:
        print("Some tests failed")
    
    test_suite.teardown()

if __name__ == "__main__":
    main()