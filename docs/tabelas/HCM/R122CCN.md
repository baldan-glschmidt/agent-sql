# R122CCN

## Descrição

Candidatos Externos - Conhecimentos

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Código do Candidato |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| SeqCcn | Number(002,0) | Não | Sequência do Conhecimento |
| DatIni | Date | Sim | Data de Ínicio do Conhecimento |
| ComCnc | String(100) | Sim | Comentário sobre Conhecimento |
| DatTre | Date | Sim | Data de Início do Treinamento no Conhecimento |
| DatVal | Date | Sim | Data de Validade do Conhecimento |
| IdiLei | String(001) | Sim | Nível Conhecimento Leitura |
| IdiEsc | String(001) | Sim | Nível Conhecimento Escrita |
| IdiCon | String(001) | Sim | Nível Conhecimento Conversação |

---

## Chave Primária

- NumCan
- FamCnc
- CodCnc
- SeqCcn

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CCN_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122CCN_002

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

