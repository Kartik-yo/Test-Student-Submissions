package app;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class UtilsTest {
    @Test
    public void testAddNumbers() {
        assertEquals(7, Utils.addNumbers(3, 4), "3 + 4 should equal 7");
    }
}
