# E205DXP

## Descrição

Estoques - Depósitos - Produtos não Permitidos

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodDep | String(010) | Não | Código do depósito |
| SeqDxp | Number(009,0) | Não | Sequência de produtos que não pode ser armazenados no depósito |
| CodOri | String(003) | Sim | Código de Origem do Produto não permitida no depósito/localização |
| CodFam | String(006) | Sim | Código da Família do Produto não permitida no depósito/localização |
| CodAge | String(005) | Sim | Código do agrupamento de estoques não permitido no depósito/localização |
| CodAgc | String(005) | Sim | Código do agrupamento comercial não permitido no depósito/localização |
| CodPro | String(014) | Sim | Código do produto não permitido no depósito/localização |
| CodDer | String(007) | Sim | Código da derivação do produto não permitida no depósito/localização |
| ObsDxp | String(250) | Sim | Texto da observação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodDep
- SeqDxp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E205DXP_001

**Tabela:** E205DEP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodDep | CodDep |

