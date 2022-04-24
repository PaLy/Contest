package codejam.s2022.round1a.a

import org.junit.Test
import org.junit.runner.RunWith
import org.junit.runners.Parameterized
import java.io.ByteArrayOutputStream
import java.io.File
import java.io.PrintStream
import java.nio.charset.StandardCharsets
import kotlin.test.assertEquals

@RunWith(Parameterized::class)
class SolutionTest(private val inputFile: String, private val outputFile: String) {
    companion object {
        @JvmStatic
        @Parameterized.Parameters
        fun data(): Collection<Array<Any>> {
            return (
                File(".")
                    .list()!!
                    .filter { it.endsWith(".in") }
                    .map { arrayOf(it, it.substringBeforeLast(".in") + ".out") }
            )
        }
    }

    @Test
    fun test() {
        val input = File(inputFile).inputStream()

        val utf8 = StandardCharsets.UTF_8.name()
        val baos = ByteArrayOutputStream()
        val printStream = PrintStream(baos, true, utf8)

        solve(input, printStream)

        val output = baos.toString(utf8)
        val expectedOutput = File(outputFile).readText()

        assertEquals(expectedOutput, output)
    }
}