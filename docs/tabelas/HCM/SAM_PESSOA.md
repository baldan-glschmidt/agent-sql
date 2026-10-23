# SAM_PESSOA

## Descrição

Tabela de pessoas do SAMSenior que serão replicadas para a G5

---

## Resumo

- Campos: 24
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ID_PESSOA | Number(009,0) | Não | Identificador da pessoa no SAMSenior |
| NOME | String(100) | Não | Nome da pessoa no SAMSenior |
| GENERO | String(001) | Sim | Sexo da pessoa no SAMSenior |
| DATA_NASCIMENTO | Date | Sim | Data de nascimento |
| MATRICULA | String(020) | Sim | Matrícula |
| DATA_CADASTRO | Date | Sim | Data e hora do cadastro no SAMSenior |
| ENDERECO | String(200) | Sim | Logradouro |
| NUMERO_ENDERECO | String(010) | Sim | Número residencial |
| BAIRRO | String(030) | Sim | Bairro |
| CIDADE | String(030) | Sim | Cidade |
| UF | String(030) | Sim | UF |
| CEP | String(020) | Sim | CEP |
| NACIONALIDADE | String(050) | Sim | Nacionalidade |
| DATA_ULTIMO_ACESSO | Date | Sim | Data e hora do último acesso |
| SITUACAO | Number(001,0) | Sim | Situação, 1 ativo, 0 bloqueado |
| RG | String(016) | Sim | Número do RG |
| CPF | String(011) | Sim | Número do CPF |
| CNH | String(020) | Sim | Número do CNH |
| PIS | String(011) | Sim | Número do PIS |
| EMAIL | String(050) | Sim | E-mail |
| DDI | Number(003,0) | Sim | DDI |
| TELEFONE | String(025) | Sim | Telefone |
| RAMAL | String(005) | Sim | Ramal |
| PAPEL | String(050) | Não | Nome do papel |

---

## Chave Primária

- ID_PESSOA

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
