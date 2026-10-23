# R121DOC

## Descrição

Concurso - Documentos necessários

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| SeqDoc | Number(002,0) | Não | Sequência de Documento |
| NomDoc | String(040) | Sim | Nome do documento |
| ObsDoc | String(250) | Sim | Observação sobre documento |
| IndObr | String(001) | Sim | Indicador de obrigatoriedade |

---

## Chave Primária

- AnoCon
- NumCon
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121DOC_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

