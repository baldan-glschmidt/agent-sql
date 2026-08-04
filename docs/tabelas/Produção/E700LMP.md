# E700LMP

## Descrição

Ficha - Modelo - Liga Modelo X Produto

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodMod | String(014) | Não | Código do Modelo |
| CodPro | String(014) | Não | Código do Produto Composto associado ao Modelo |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção onde o componente é agregado ao Produto Composto |
| SeqMod | Number(004,0) | Não | Sequência lógica  onde o componente é utilizado na fabricação do Produto |
| CodCmp | String(014) | Não | Código do Componente (Produto) agregado ao Modelo |
| DerCmp | String(007) | Sim | Derivação do Componente VARIÁVEL (p/ cada Produto Composto associado ao Modelo) |
| DatAlt | Date | Sim | Data da Geração ou Alteração da ligação Modelo X Produto |
| CodUsu | Number(010,0) | Sim | Código do Usuário que alterou |

---

## Chave Primária

- CodEmp
- CodMod
- CodPro
- CodEtg
- SeqMod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700LMP_002

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E700LMP_004

**Tabela:** E700CMM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |
| CodEtg | CodEtg |
| SeqMod | SeqMod |

### IR_E700LMP_005

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCmp | CodPro |

