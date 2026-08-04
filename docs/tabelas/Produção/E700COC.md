# E700COC

## Descrição

Ficha - Modelo - Coordenadas do Componente

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção onde  o componente é agregado ao Produto composto |
| SeqMod | Number(004,0) | Não | Sequência lógica que o componente é utilizado na fabricação do Produto composto |
| SeqCoc | Number(004,0) | Não | Sequência lógica de inclusão das coordenadas do componente |
| PosCo1 | Number(008,2) | Sim | Primeira Posição da Coordenada do Componente |
| PosCo2 | Number(008,2) | Sim | Segunda Posição da Coordenada do Componente |
| PosCo3 | Number(008,2) | Sim | Terceira Posição da Coordenada do Componente |
| DatAlt | Date | Não | Data Geração/Alteração |
| HorAlt | Number(005,0) | Sim | Hora da geração/alteração do registro |
| CodUsu | Number(010,0) | Sim | Código do Usuário da Geração/Alteração |

---

## Chave Primária

- CodEmp
- CodMod
- CodEtg
- SeqMod
- SeqCoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700COC_001

**Tabela:** E700MOD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |

### IR_E700COC_002

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

### IR_E700COC_003

**Tabela:** E700CMM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |
| CodEtg | CodEtg |
| SeqMod | SeqMod |

