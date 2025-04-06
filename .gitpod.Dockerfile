# .gitpod.Dockerfile
FROM gitpod/workspace-full

# Install Solana CLI
RUN sh -c "$(curl -sSfL https://release.solana.com/stable/install)"
ENV PATH="/home/gitpod/.local/share/solana/install/active_release/bin:$PATH"

# Install Anchor
RUN rustup component add rustfmt && \
    cargo install --git https://github.com/coral-xyz/anchor anchor-cli --locked

# Preload Solana Test Validator
RUN solana --version && anchor --version
