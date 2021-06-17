import generator as g

if __name__ == '__main__':

    for i in range(5):
        name = g.names()
        g.logger.info("[Name chosen.]")
        title = g.titles()
        g.logger.info("[Title chosen.]")
        g.logger.info(f"Sir {name} the {title}")
