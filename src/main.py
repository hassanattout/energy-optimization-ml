from generate_data import main as generate_data
from optimize import main as optimize
from train import main as train


def main() -> None:
    print("1/3 Generating reproducible synthetic data")
    generate_data()
    print("2/3 Training and evaluating the forecasting model")
    train()
    print("3/3 Applying the load-shifting heuristic")
    optimize()


if __name__ == "__main__":
    main()
