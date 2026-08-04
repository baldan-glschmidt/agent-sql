# E075MAE

## Descrição

Cadastros - Produtos - Informações de Manuseio, Armazenagem e Embalagem

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do Produto (tamanho, cor, etc.) |
| QtdEmb | Number(010,4) | Sim | Quantidade por embalagem |
| EmpMax | Number(004,0) | Sim | Empilhamento máximo permitido |
| ForEmp | String(100) | Sim | Forma de empilhamento (descritivo) |
| ConAmb | String(100) | Sim | Condições ambientais para armazenagem |
| CuiMan | String(100) | Sim | Cuidados para Manuseio |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E075MAE_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E075MAE_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E075MAE_002

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

