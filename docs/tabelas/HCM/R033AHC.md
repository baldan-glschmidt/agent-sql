# R033AHC

## Descrição

Histórico de Competências da Pessoa - Anexos

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| SeqHis | Number(008,0) | Não | Informe um número sequencial para identificar o histórico |
| SeqAne | Number(002,0) | Não | Sequência do anexo |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| ArqAne | Image | Sim | Arquivo anexo |

---

## Chave Primária

- CodPes
- SeqHis
- SeqAne

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033AHC_001

**Tabela:** R033HCP

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |
| SeqHis | SeqHis |

