program Player;
Uses sysutils,math;
Type
    Dir = Record
                x,y:integer;
                str:string;
               End;
var
    n,rows,cols,a,cx,cy,tx,ty,kr,kc,i : integer;
    next:string;
    maze: Array[1..100] of string;
    DIRS: Array[1..4] of Dir;
    
Procedure update();
var i,j:integer;
Begin
    for i:=1 to rows do 
        for j:=1 to cols do begin
            if maze[i][j] = 'C' then begin
                cx := i;
                cy := j;
            end else if maze[i][j] = 'T' then begin
                tx := i;
                ty := j;
            end;
        end;
End;

Function Valid(x,y:integer):boolean;
begin
    if (0 <= x) and (x < rows) and (0 <=y) and (y < cols) and (maze[x][y] <>'?') and (maze[x][y]<>'#') then
        valid := True
    else
        valid:=False;
end;

Function shortest_path(sx,sy,ex,ey:integer;ff:boolean):string;
var dist:array[1..100][1..200] of integer;
fr:array[1..100][1..200] of integer;
pr:array[1..100][1..200] of string;
queue:array of integer;
curpos:integer;
begin
    dist[sx][sy]:=0;
    setlength(queue, 100000000);
    curpos:=0;
    not_found = True
    while queue and not_found:
        pos = queue.popleft()
        for d in DIRS:
            nx = pos[0] + d[0]
            ny = pos[1] + d[1]
            npos = (nx, ny)
            if (valid(nx, ny) and npos not in dist) or (first_quot and is_in(nx, ny) and maze[nx][ny] == '?'):
                dist[npos] = dist[pos] + 1
                fr[npos] = pos
                pr[npos] = d[2]
                queue.append(npos)

                if first_quot and maze[nx][ny] == '?':
                    ex = nx
                    ey = ny
                if nx == ex and ny == ey:
                    not_found = False
                    break
    cur_pos = (ex, ey)
    if cur_pos in dist:
        path = []
        while cur_pos != (sx, sy):
            path.append(pr[cur_pos])
            cur_pos = fr[cur_pos]

        path = list(reversed(path))
        print(path, file=sys.stderr)
        return path
    else:
        return None
end;

Function max_quot(kr,kc:integer):string;
var resc,nr,nc,c,d,i,j:integer;
res:string;
Begin
    resc := -1;
    for d:=1 to 4 do begin
        nr := kr + DIRS[d].x;
        nc := kc + DIRS[d].y;
        if valid(nr, nc) then begin
            c := 0;
            for i:=max(1, nr-2) to min(rows, nr + 2) do
                for j:=max(1, nc - 2) to min(cols, nc + 2) do begin
                    if maze[i][j] = '?' then
                            c := c+1;
                    if c >= resc then begin
                        resc := c;
                        res := DIRS[d].str;
                    end;
                end;
        end;
    end;
    if resc > 0 then begin
        max_quot:=res;
        writeln(Stderr, res);
    end else begin
        writeln(stderr, 'nie');
        max_quot:=shortest_path(kr, kc, -1, -1, True);
    end;
end;

begin
    // Read init information from standard input, if any
    readln(rows, cols, a);
    cx:=-1;
    DIRS[1].x := 0;
    DIRS[1].y := 1;
    DIRS[1].str := 'RIGHT';
    DIRS[2].x := 0;
    DIRS[2].y := -1;
    DIRS[2].str := 'LEFT';
    DIRS[3].x := -1;
    DIRS[3].y := 0;
    DIRS[3].str := 'UP';
    DIRS[4].x := 1;
    DIRS[4].y := 0;
    DIRS[4].str := 'DOWN';
    while true do
        begin
        // Read information from standard input
        readln(kr, kc);
        kr +=1;
        kc+=1;
        for i:=1 to rows do readln(maze[i]);
        update();
        
        if cx <> -1 then begin
        
        end else begin
            next:= max_quot(kr,kc);
            writeln(next);
        end;

        // writeln(StdErr, 'Debug messages...');
        flush(StdErr); // DO NOT REMOVE

        // Write action to standard output
        writeln('RIGHT');
        flush(output); // DO NOT REMOVE
        end;
end.
