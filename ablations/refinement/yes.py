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
        # re-write the buggy code: losses.append(loss)
        losses.append(loss.item())
        # re-write the buggy code: loss.foward()
        loss.backward()
        # re-write the buggy code: optimizer.step(step=epoch)
        optimizer.step()
        if batch_idx % print_every == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(dataloader.dataset),
                100. * batch_idx / len(dataloader), loss.item()))
    return losses
