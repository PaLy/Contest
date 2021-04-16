/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var inputs = readline().split(' ');
var width = parseInt(inputs[0]); // width of the firewall grid
var height = parseInt(inputs[1]); // height of the firewall grid
var mapa = [];
for (var i = 0; i < height; i++) {
    var mapRow = readline(); // one line of the firewall grid
    mapa.push(mapRow)
}

var die_time = [];
for (var i = 0; i < height; i++) {
    var dt = [];
    for (var j = 0; j < width; j++) {
        dt.push(-1);
    }
    die_time.push(dt);
}

function left(x, y) {
    var res = [];
    for (var i = x - 1; i >= x - 3 && i >= 0; i--) {
        res.push([i, y]);
    }
    return res;
}

function right(x, y) {
    var res = [];
    for (var i = x + 1; i < height && i < x + 4; i++) {
        res.push([i, y]);
    }
    return res;
}

function up(x, y) {
    var res = [];
    for (var i = y - 1; i >= y - 3 && i >= 0; i--) {
        res.push([x, i]);
    }
    return res;
}

function down(x, y) {
    var res = [];
    for (var i = y + 1; i < width && i < y + 4; i++) {
        res.push([x, i]);
    }
    return res;
}

function how_many_to_destroy(x, y) {
    function inner(pos) {
        var x = pos[0];
        var y = pos[1];
        if (mapa[x][y] == '@' && die_time[x][y] < 1) {
            res += 1;
        }
        if (mapa[x][y] == '#') {
            return false;
        }
        return true;
    }

    var res = 0;
    for(var pos in left(x,y)) {
        if (!inner(pos)) {
            break;
        }
    }
    for(var pos in right(x,y)) {
        if (!inner(pos)) {
            break;
        }
    }
    for(var pos in up(x,y)) {
        if (!inner(pos)) {
            break;
        }
    }
    for(var pos in down(x,y)) {
        if (!inner(pos)) {
            break;
        }
    }
}


var explode_time = function (rounds, x, y) {
    function inner(pos) {
        var res = 0;
        
    }

    left(x,y).forEach(inner(pos));
};

function choose_by_explode_time(rounds, x, y) {
    var n = x.length;
    var best = 0;
    var resi = 0;
    var resj = 0;
    for (var i = 0; i < n; i++) {
        var t = explode_time(rounds, x[i], y[i]);
        if (t > best) {
            best = t;
            resi = x[i];
            resj = x[j];
        }
    }
    return [best, resi, resj];
}

// game loop
while (true) {
    var inputs = readline().split(' ');
    var rounds = parseInt(inputs[0]); // number of rounds left before the end of the game
    var bombs = parseInt(inputs[1]); // number of bombs left

    // Write an action using print()
    // To debug: printErr('Debug messages...');

    remove_exploded_bombs();
    var ma = 0;
    var ri = [];
    var rj = [];
    for (var i = 0; i < height; i++) {
        for (var j = 0; j < width; j++) {
            if (mapa[i][j] == '.') {
                var c = how_many_to_destroy(x, y);
                if (c > ma) {
                    ri = [i];
                    rj = [j];
                } else if (c == ma) {
                    ri.push(i);
                    rj.push(j);
                }
            }
        }
    }
    if (ma == 0) {
        print('WAIT');
    } else {
        var rrr = choose_by_explode_time(rounds, ri, rj);
        update_map(rrr[0], rrr[1], rrr[2]);
        print(rrr[2] + ' ' + rrr[1]);
    }
}