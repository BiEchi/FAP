def train(dataloader, optimizer, epoch, print_every):
    losses = []
    model.train()
    # YOUR CODE HERE
    for batch_idx, data in enumerate(dataloader):
        optimizer.zero_grad()
        x, y = data
        x, y = Variable(x), Variable(y)
        output = model(x)
        loss = criterion(output, y)
        losses.append(loss) # buggy
        loss.forward() # buggy
        optimizer.step(step=epoch) # buggy
        if batch_idx % print_every == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(dataloader.dataset),
                100. * batch_idx / len(dataloader), loss.item()))
    return losses
