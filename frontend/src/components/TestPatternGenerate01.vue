<template>
  <div class="test-pattern-generate-01">
    <h1>テストパターン生成01</h1>
    <form class="me-5">
      <div v-for="column in columnsCount" :key="column">
      <h3>列{{column}}</h3>
        <div class="row">
          <div class="col-1 mb-3">
            <label class="form-label">タイトル</label>
          </div>
          <div class="col-6 mb-3">
            <input v-model="columnsTitles[column-1]" class="form-control" type="text">
          </div>
        </div>

        <div v-for="row in rowsCount[column-1]" :key="row">
          <div class="row">
            <div class="col-1 mb-3">
              <label class="form-label">項目{{row}}</label>
            </div>
            <div class="col-6 mb-3">
              <input v-model="rowsTitles[column-1][row-1]" class="form-control" type="text">
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col-1 mb-3">
          </div>
          <div class="col mb-3">
            <button type="button" @click="IncrementRowItem(column)" class="btn btn-outline-primary mb-2 me-2">項目を追加</button>
            <button type="button" @click="DecrementRowItem(column)" class="btn btn-outline-primary mb-2 me-2">項目を削除</button>
          </div>
        </div>
      </div>  <!-- v-for columnsCount end -->
      <div>
        <button type="button" @click="IncrementColmun()" class="btn btn-outline-danger mb-2 me-2">列を追加</button>
        <button type="button" @click="DecrementColmun()" class="btn btn-outline-danger mb-2 me-2">列を削除</button>
      </div>
      <div>
        <button type="button" @click="GenerateTestPatarn()" class="btn btn-primary">パターン生成</button>
      </div>
    </form>

    <hr>
    <!-- {{pattans}} -->
    <table class="table mb-3">
      <thead>
        <tr>
          <th v-for="headerItem in headers" :key="headerItem" scope="col">
            {{headerItem}}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in pattans" :key="row">
          <td v-for="item in row" :key="item">
            {{item}}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      columnsCount: 1,
      rowsCount: [1],
      columnsTitles: [],
      rowsTitles: [ //max30列
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
      ],
      headers: ["No"],
      pattans: [],
    }
  },
  methods: {
    //難しい。いいロジックを考える
    //3列×3行の時うまく計算されない
    GenerateTestPatarn() {
      console.log(this.columnsTitles)
      console.log(this.rowsTitles)

      let rowPotinter = []
      let shouldInsertedPos = []
      let firstInsertedPos = []
      console.log(this.columnsCount)
      for (let col = 0; col < this.columnsCount; col++) {
        console.log("col：" + col)
        for (let row = 0; row < this.rowsTitles[col].length; row++) {
          console.log("row：" + row)
          console.log("this.rowsTitles[col].length：" + this.rowsTitles[col].length) //
          //ポインタ生成
          if (col == 0) {  //
            rowPotinter.push([row])
            //shouldInsertedPos.push(row+1)
            //firstInsertedPos.push(row+1)
            console.log("rowPotinter.push([row]):"+row)
          } else {  //col != 0 の場合
              if (row == 0) {
                shouldInsertedPos = []  //ここでクリア
                for (let ptcol = 0; ptcol < rowPotinter.length; ptcol++) {
                  rowPotinter[ptcol].push(row)
                  console.log("rowPotinter[ptcol].push(row):"+row)
                  shouldInsertedPos.push(ptcol+1)
                  console.log("shouldInsertedPos.push(ptcol+1):")
                  console.log(ptcol+1)
                  firstInsertedPos = shouldInsertedPos
                  //console.log("rowPotinter:"+rowPotinter)
                  //console.log(rowPotinter)
                }
              } else {  //row != 0 の場合
                //バグがある
                console.log("shouldInsertedPos:")
                console.log(shouldInsertedPos)
                console.log("shouldInsertedPos.length:" + shouldInsertedPos.length)
                let insertedRowCnt = 0
                for (let i = 0; i < shouldInsertedPos.length; i++) {
                  console.log("insertedRowCnt:" +insertedRowCnt)

                  let fetchPos = shouldInsertedPos[i]-1+insertedRowCnt
                  console.log("fetchPos:"+fetchPos)
                  //let willCopyedArray = rowPotinter[shouldInsertedPos[i]-1+insertedRowCnt]
                  //console.log("willCopyedArray:")
                  //console.log(willCopyedArray)
                  console.log("rowPotinter[fetchPos].length:"+rowPotinter[fetchPos].length)
                  let pos = rowPotinter[fetchPos].length
                  pos = pos -1
                  console.log("pos:"+pos)
                  console.log("rowPotinter[fetchPos]:"+rowPotinter[fetchPos])
                  let originArray = rowPotinter[fetchPos]
                  console.log("originArray:"+originArray)
                  let newArray = Array.from(originArray)
                  newArray.splice(pos, 1, row)
                  console.log("newArray:"+newArray)
                  //rowPotinter[fetchPos].splice(pos, 1, row) //NG ここ編集したらダメ
                  
                  console.log("shouldInsertedPos[i]:"+shouldInsertedPos[i])
                  console.log("insertedRowCnt:"+insertedRowCnt)
                  pos = shouldInsertedPos[i] + insertedRowCnt
                  console.log("pos:"+pos)
                  rowPotinter.splice(pos, 0, newArray)
                  console.log("rowPotinter:"+rowPotinter)
                  ++insertedRowCnt
                }
                
                //shouldInsertedPos 更新
                //列が変わると、この計算は不要になる。位置要検討
                let nextInsertedPos = firstInsertedPos.map(x => x * (row+1))
                console.log("nextInsertedPos:")
                console.log(nextInsertedPos)
                shouldInsertedPos = nextInsertedPos
                console.log("shouldInsertedPos:")
                console.log(shouldInsertedPos)
              }
          }
          console.log("rowPotinter:"+rowPotinter)
          console.log(rowPotinter)
        }
      }
      console.log("rowPotinter:")    
      console.log(rowPotinter)    

      //ポインターが示す項目を取得
      console.log("this.rowsTitles:")
      console.log(this.rowsTitles)
      console.log("rowPotinter.length:" + rowPotinter.length)
      let No = 1
      for (let col = 0; col < rowPotinter.length; col++) {
        this.pattans[col] = []
        for (let row = 0; row < rowPotinter[col].length; row++) {
          //console.log("rowPotinter[col]:")
          //console.log(rowPotinter[col])
          //console.log("rowPotinter[col][row]:")
          //console.log(rowPotinter[col][row])
          this.pattans[col].push(this.rowsTitles[row][rowPotinter[col][row]])
        }
        //列の先頭にNoを付加
        this.pattans[col].unshift(No)
        ++No
      }

      //ヘッダー行
      for (let col = 0; col < this.columnsCount; col++) {
        this.headers.push(this.columnsTitles[col])
      }
      console.log("this.pattans:")
      console.log(this.pattans)

/*
      //rowPotinter
      //取り出す順番を決定する
      //例
      //[0,0,0]
      //[0,0,1]
      //[0,0,2]
      //[1,0,0]
      //[1,0,1]
      //[1,0,2]

*/

  },
    IncrementColmun() {
      if(this.columnsCount < 30){
        this.columnsCount++
        //console.log(this.rowsCount)
        this.rowsCount.push(1)
        //console.log(this.rowsCount)
      }
    },
    DecrementColmun() {
      if(this.columnsCount > 1){
        this.columnsCount--
        //console.log(this.rowsCount)
        this.rowsCount.pop()
        //console.log(this.rowsCount)
      }
    },
    IncrementRowItem(column) {
      let cnt = this.rowsCount[column-1]
      console.log(cnt)
      ++cnt
      console.log(cnt)
      let new_array = this.rowsCount.splice(column-1, 1, cnt)
      console.log(new_array)
      console.log(this.rowsCount)
    },
    DecrementRowItem(column) {
      let cnt = this.rowsCount[column-1]
      if(cnt > 1){
        cnt--
      }
      let new_array = this.rowsCount.splice(column-1, 1, cnt)
      console.log(new_array)
      console.log(this.rowsCount)
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
