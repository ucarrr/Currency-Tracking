import { StyleSheet, Text, View, FlatList } from 'react-native'
import React, { useState, useEffect } from 'react'


//http://192.168.1.15:5000/api/doviz  - http://10.0.5.8:5000/api/doviz
const App = () => {
  const [data, setData] = useState([]);
  const getData = () => {
    return fetch('http://192.168.1.7:5000/api/doviz')
      .then((response) => response.json())
      .then((json) => {
        var manipulatedData = Object.keys(json).map(key => {
          return json[key];
        });
        setData(manipulatedData);
        console.log(manipulatedData)
      })
      .catch((error) => {
        console.error(error);
      });
  };
  useEffect(() => {
    getData();
  }, []);
  return (
    <View>
      <FlatList
        data={data}
        key={(item) => item.id.toString()}
        numColumn={4}
        ListEmptyComponent={() => <View><Text>Veri Yok</Text></View>}
        renderItem={({ item }) =>
          <View style={styles.container}>
            <View style={styles.styletitle}>

              <View style={styles.box}>
                <Text style={styles.texts}><Text style={styles.boldText}>isim : </Text>{item.isim}</Text>
              </View>
              <View style={styles.box}>
                <Text style={styles.texts}><Text style={styles.boldText}>CurrencyName :</Text> {item.CurrencyName}</Text>
              </View>
              <View style={styles.box}>
                <Text style={styles.texts}><Text style={styles.boldText}>Kod :</Text> {item.Kod}</Text>
              </View>
              <View style={styles.box}>
                <Text style={styles.texts}><Text style={styles.boldText}>BanknoteBuying :</Text>{item.BanknoteBuying}</Text>
              </View>
              <View style={styles.box}>
                <Text style={styles.texts}><Text style={styles.boldText}>BanknoteSelling :</Text> {item.BanknoteSelling}</Text>
              </View>
              <View style={styles.box}>
                <Text style={styles.texts}><Text style={styles.boldText}>CrossRateUSD :</Text> {item.CrossRateUSD}</Text>
              </View>

              <View style={styles.box}>
                <Text style={styles.texts}><Text style={styles.boldText}>ForexBuying :</Text> {item.ForexBuying}</Text>
              </View>
              <View style={styles.box}>
                <Text style={styles.texts}><Text style={styles.boldText}>ForexSelling : </Text>{item.ForexSelling}</Text>
              </View>



            </View>
          </View>
        }
      />
    </View>
  )
}

export default App

const styles = StyleSheet.create({
  boldText: {
    fontWeight: 'bold',
  
  },
  texts:{
    fontSize: 18,
     
  },
  container: {
    padding: 10,
    flex: 1,
    backgroundColor: '#ecf0f1',
    textAlign: 'left',
    alignItems: 'flex-start',
    justifyContent: 'flex-start',
    borderRadius: 10,
    margin: 15,
    borderColor: '#ddd'

  },
  styletitle: {
    padding: 5,
    flex: 1,
 
    marginBottom: 5,
    borderRadius: 10,


  },
  box: {

  },

})