import os

from Models.ModelsBuilders import ModelsBuilders

DIRECTORY = r'.\Data sources'
SOURCE_EXTENSION = '.csv'
TARGET_DATA = 'Adj Close'


def read_all_datasets(directory: str,
                      extension: str) -> list[str]:
    return [file
            for file in os.listdir(directory)
            if file.endswith(extension)]


def main():
    sources = read_all_datasets(DIRECTORY, SOURCE_EXTENSION)
    for source in sources:
        for size in [0.3, 0.6, 0.9]:
            ModelsBuilders.create_arima().set_source(os.path.join(DIRECTORY, source)).to_target(TARGET_DATA)\
                .with_test_size(size).train().save()


if __name__ == '__main__':
    main()
