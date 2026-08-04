# E700NSR

## Descrição

Ficha - Modelo - Narrativa por Seq. Componente

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção onde  o componente é agregado ao Produto composto |
| SeqMod | Number(004,0) | Não | Sequência lógica que o componente é utilizado na fabricação do Produto composto |
| SeqNsr | Number(004,0) | Não | Número sequencial da linha da narrativa sobre a sequência do componente |
| CodNof | String(006) | Sim | Código da Narrativa automática p/ operação (Instruções de trabalho) |
| DesNsr | String(999) | Sim | Descrição técnica da sequência operacional (descrição do processo) |
| DatAlt | Date | Não | Data de Geração/Alteração da sequência |
| CodUsu | Number(010,0) | Sim | Usuário que alterou |

---

## Chave Primária

- CodEmp
- CodMod
- CodEtg
- SeqMod
- SeqNsr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700NSR_001

**Tabela:** E700MOD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |

### IR_E700NSR_002

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

