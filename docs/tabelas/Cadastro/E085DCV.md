# E085DCV

## Descrição

Cadastros - Clientes - Convênios - Dependentes

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do cliente |
| CodCnv | Number(004,0) | Não | Código do convênio |
| DepCnv | Number(004,0) | Não | Código do Dependente |
| DepNom | String(100) | Não | Nome do Dependente |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do dependente |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do dependente |
| DepCcn | String(020) | Sim | Número do cartão do convênio |
| DepCpl | String(030) | Sim | Informação complementar ao cadastro de dependentes |
| SitDep | String(001) | Não | Situação do Dependente (Ativo ou Inativo) |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAtu | Date | Sim | Data da última alteração do registro |
| HorAtu | Number(005,0) | Sim | Hora da última alteração do registro |
| SenCnv | String(020) | Sim | Senha do conveniado no convênio |

---

## Chave Primária

- CodCli
- CodCnv
- DepCnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E085DCV_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085DCV_001

**Tabela:** E085CNV

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |
| CodCnv | CodCnv |

