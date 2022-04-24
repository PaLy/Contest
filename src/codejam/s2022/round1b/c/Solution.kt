package codejam.s2022.round1b.c

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream
import kotlin.random.Random
import kotlin.system.exitProcess

fun main() {
    solve(System.`in`, System.out)
}

fun solve(inputStream: InputStream, out: PrintStream) {
    val reader = BufferedReader(InputStreamReader(inputStream))
    val printer = PrintStream(out)
    val readLine = { reader.readLine() }
    val println = { it: String ->
        printer.println(it)
        printer.flush()
    }

    val t = readLine().toInt()
    for (i in 1..t) solveCase(i, readLine, println)
}

private fun solveCase(t: Int, readLine: () -> String, println: (String) -> Unit) {
    println("00000000")
    while (true) {
        val response = readLine().toInt()
        if (response == 0) break
        else if (response == -1) exitProcess(0)
        else {
            var guess = "00000000"
            while (guess.count { it == '1' } != response) {
                guess = Random.nextInt(0, 256).toString(2)
            }
            while (guess.length < 8) {
                guess += "0"
            }
            println(guess)
        }
    }
}
