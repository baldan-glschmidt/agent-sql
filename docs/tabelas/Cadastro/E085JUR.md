# E085JUR

## Descrição

Cadastros - Clientes - Dados Pessoa Jurídica

---

## Resumo

- Campos: 49
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do cliente |
| DatFdc | Date | Sim | Data da fundação da empresa |
| NomSo1 | String(030) | Sim | Nome do sócio 1 |
| CpfSo1 | String(025) | Sim | Número do CNPJ ou CPF do sócio 1 |
| NomSo2 | String(030) | Sim | Nome do sócio 2 |
| CpfSo2 | String(025) | Sim | Número do CNPJ ou CPF do sócio 2 |
| NomSo3 | String(030) | Sim | Nome do sócio 3 |
| CpfSo3 | String(025) | Sim | Número do CNPJ ou CPF do sócio 3 |
| QtdFun | Number(006,0) | Sim | Quantidade de funcionários |
| VlrFat | Number(014,2) | Sim | Valor do faturamento anual em dólares |
| AnoFat | Number(004,0) | Sim | Ano base do faturamento anual em dólares informado |
| NomAdi | String(030) | Sim | Administrador da empresa |
| FonAdi | String(020) | Sim | Telefone do administrador da empresa |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| FunSo1 | String(030) | Sim | Função do sócio 1 |
| FunSo2 | String(030) | Sim | Função do sócio 2 |
| FunSo3 | String(030) | Sim | Função do sócio 3 |
| CarSo1 | String(025) | Sim | Cargo do sócio 1 |
| CarSo2 | String(025) | Sim | Cargo do sócio 2 |
| CarSo3 | String(025) | Sim | Cargo do sócio 3 |
| ProSo1 | String(025) | Sim | Profissão do sócio 1 |
| ProSo2 | String(025) | Sim | Profissão do sócio 2 |
| ProSo3 | String(025) | Sim | Profissão do sócio 3 |
| EscSo1 | Number(001,0) | Sim | Estado civil do sócio 1 |
| EscSo2 | Number(001,0) | Sim | Estado civil do sócio 2 |
| EscSo3 | Number(001,0) | Sim | Estado civil do sócio 3 |
| CidSo1 | String(060) | Sim | Cidade de residência do sócio 1 |
| CidSo2 | String(060) | Sim | Cidade de residência do sócio 2 |
| CidSo3 | String(060) | Sim | Cidade de residência do sócio 3 |
| RgeSo1 | String(013) | Sim | Número do documento de identidade (RG) do sócio 1 |
| RgeSo2 | String(013) | Sim | Número do documento de identidade (RG) do sócio 2 |
| RgeSo3 | String(013) | Sim | Número do documento de identidade (RG) do sócio 3 |
| OrgSo1 | String(005) | Sim | Órgão emissor do RG do sócio 1 |
| OrgSo2 | String(005) | Sim | Órgão emissor do RG do sócio 2 |
| OrgSo3 | String(005) | Sim | Órgão emissor do RG do sócio 3 |
| ParSo1 | Number(005,2) | Sim | Percentual de participação do sócio 1 no capital social |
| ParSo2 | Number(005,2) | Sim | Percentual de participação do sócio 2 no capital social |
| ParSo3 | Number(005,2) | Sim | Percentual de participação do sócio 3 no capital social |
| GerSo1 | String(001) | Sim | Indicativo se o sócio 1 participa da gerência |
| GerSo2 | String(001) | Sim | Indicativo se o sócio 2 participa da gerência |
| GerSo3 | String(001) | Sim | Indicativo se o sócio 3 participa da gerência |
| FonSo1 | String(020) | Sim | Telefone Sócio 1 |
| FonSo2 | String(020) | Sim | Telefone Sócio 2 |
| FonSo3 | String(020) | Sim | Telefone Sócio 3 |
| ObsSo1 | String(999) | Sim | Observação referente ao sócio 1 |
| ObsSo2 | String(999) | Sim | Observação referente ao sócio 2 |
| ObsSo3 | String(999) | Sim | Observação referente ao sócio 3 |

---

## Chave Primária

- CodCli

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E085JUR_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

