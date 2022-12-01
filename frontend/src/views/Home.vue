<template>
    <main>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 p-4 gap-4 bg-white dark:bg-gray-200">
            <div class="bg-blue-500 dark:bg-gray-800 shadow-lg rounded-md flex items-center justify-between p-3 border-b-4 border-blue-600 dark:border-gray-600 text-white font-medium group">
              <div class="flex justify-center items-center w-14 h-14 bg-white rounded-full transition-all duration-300 transform group-hover:rotate-12">
                <BusinessplanIcon class="text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"/>
                <!-- <svg width="30" height="30" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="stroke-current text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg> -->
              </div>
              <div class="text-right">
                <p class="text-2xl">$ 1,257</p>
                <p>Ingresos</p>
              </div>
            </div>
            <div class="bg-green-500 dark:bg-gray-800 shadow-lg rounded-md flex items-center justify-between p-3 border-b-4 border-green-600 dark:border-gray-600 text-white font-medium group">
              <div class="flex justify-center items-center w-14 h-14 bg-white rounded-full transition-all duration-300 transform group-hover:rotate-12">
                <CarIcon class="text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"/>
              </div>
              <div class="text-right">
                <p class="text-2xl">557</p>
                <p>Terminadas</p>
              </div>
            </div>
            <div class="bg-yellow-500 dark:bg-gray-800 shadow-lg rounded-md flex items-center justify-between p-3 border-b-4 border-yellow-600 dark:border-gray-600 text-white font-medium group">
              <div class="flex justify-center items-center w-14 h-14 bg-white rounded-full transition-all duration-300 transform group-hover:rotate-12">
                <CarIcon class="text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"/>
              </div>
              <div class="text-right">
                <p class="text-2xl">$11,257</p>
                <p>Pendientes</p>
              </div>
            </div>
            <div class="bg-gray-500 dark:bg-gray-800 shadow-lg rounded-md flex items-center justify-between p-3 border-b-4 border-gray-600 dark:border-gray-600 text-white font-medium group">
              <div class="flex justify-center items-center w-14 h-14 bg-white rounded-full transition-all duration-300 transform group-hover:rotate-12">
                <CarOffIcon class="text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"/>
              </div>
              <div class="text-right">
                <p class="text-2xl">$75,257</p>
                <p>Anuladas</p>
              </div>
            </div>
      </div>
    </main>

    <Bar
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
  </template>
  
<script setup>
import { BusinessplanIcon, CarIcon, CarOffIcon } from 'vue-tabler-icons'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const name = 'BarChart'

const components = { Bar }

const props =  {
    chartId: {
      type: String,
      default: 'bar-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Array,
      default: () => []
    }
  }

const chartData = {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ]
      }
const chartOptions = {
        responsive: true
      }

// export default {
//   name: 'BarChart',
//   components: { Bar },
//   props: {
//     chartId: {
//       type: String,
//       default: 'bar-chart'
//     },
//     datasetIdKey: {
//       type: String,
//       default: 'label'
//     },
//     width: {
//       type: Number,
//       default: 400
//     },
//     height: {
//       type: Number,
//       default: 400
//     },
//     cssClasses: {
//       default: '',
//       type: String
//     },
//     styles: {
//       type: Object,
//       default: () => {}
//     },
//     plugins: {
//       type: Array,
//       default: () => []
//     }
//   },
//   data() {
//     return {
//       chartData: {
//         labels: [ 'January', 'February', 'March' ],
//         datasets: [ { data: [40, 20, 12] } ]
//       },
//       chartOptions: {
//         responsive: true
//       }
//     }
//   }
// }
</script>

