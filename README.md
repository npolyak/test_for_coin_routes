# How to Run the code

1. Clone the repository locally by using the following command:
   clone https://github.com/npolyak/test_for_coin_routes.git
   It will create a local repository <b>test_for_coin_routes</b> into which you should cd. 
3. Make sure you have Python 3.13.5 (or higher) installed. I installed it using miniconda
4. Create a virtual environment e.g by running
   conda create -name CoinRoutes_env python=3.13.5
5. Now make sure you are in the right repository (<b>test_for_coin_routes</b>) and activate the virtual environment by doing
   conda activate CoinRoutes_env
6. Now install a missing package httpx:
   pip install httpx
7. Finally to run the python type e.g.
   python main.py -qty 22

   
