import math

def getSeatIDPart1(boardingPass):
    seatId = []

    for i in range(len(boardingPass)):
        final_row = 0
        final_col = 0
        row_min = 0
        row_max = 127
        col_min = 0
        col_max = 7
        
        for j in range(7):
            if boardingPass[i][j] == 'F':
                row_max = math.floor((row_max - row_min) / 2) + row_min
            elif boardingPass[i][j] == 'B':
                row_min = math.ceil((row_max - row_min) / 2) + row_min

        if boardingPass[i][6] == 'F':
            final_row = row_max
        elif boardingPass[i][6] == 'B':
            final_row = row_min

        for k in range(7, len(boardingPass[i])):
            if boardingPass[i][k] == 'L':
                col_max = math.floor((col_max - col_min) / 2) + col_min
            elif boardingPass[i][k] == 'R':
                col_min = math.ceil((col_max - col_min) / 2) + col_min

        if boardingPass[i].strip()[-1] == 'R':
            final_col = col_max
        elif boardingPass[i].strip()[-1] == 'L':
            final_col = col_min

        seatId.append(final_row * 8 + final_col)  
    
    return seatId
    
        
def main():
    boardingPass = []
    with open('input.txt') as f:
        for line in f:
            boardingPass.append(line.replace("\n",""))

    seatIds = getSeatIDPart1(boardingPass)
    print(f'Part 1 - Highest seat id: {max(seatIds)}')
    
    for seat in range(min(seatIds), max(seatIds)+1):
        if seat not in seatIds:
            print(f'Part 2 - Seat id: {seat}')

if __name__ == "__main__":
    main()