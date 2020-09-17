import argparse
import cityflow

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, default='low_manhattan_sim')
    args = parser.parse_args()
    eng = cityflow.Engine(f"{args.dir}/config.json", thread_num=1)
    for i in range(100):
        print("\nStep", i, "\n")

        vehicleCount = eng.get_vehicle_count()
        waitingVehiclesPerLane = eng.get_lane_waiting_vehicle_count()
        averageTravelTime = eng.get_average_travel_time()
        vehicleIDs = eng.get_vehicles(include_waiting = True)

        if vehicleCount > 0:
            vehicle0 = vehicleIDs[0]
            print(vehicle0['route'])




#        if vehicleCount > 0:
#
#            for vehicle in vehicleIDs:
#                vehicleInfo = eng.get_vehicle_info(vehicle)
#                if vehicleInfo['running'] != '0':
#                    if float(vehicleInfo['speed']) < 0.4:
#                        print('Car', vehicle, 'is standing still at intersection', vehicleInfo['intersection'])


        eng.next_step()
