def main():
    scores = [78, 85, 90, 66, 88]
    total = sum(scores)
    average = total / len(scores)

    print("=== main/master branch output ===")
    print(f"score: {scores}")
    print(f"sum: {total}")
    print(f"average: {average}")


if __name__ == "__main__":
    main()