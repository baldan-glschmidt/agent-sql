# R584EPI

## Descrição

Manutenção do Inventário de Riscos - GHEs - Riscos - EPIs

---

## Resumo

- Campos: 7
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInv | Number(007,0) | Não | Código do Inventário de Riscos |
| NumAmb | Number(007,0) | Não | Código do Ambiente de Trabalho |
| DatInv | Date | Não | Data do Inventário de Riscos |
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| SeqRis | Number(006,0) | Não | Sequência do risco |
| CodEpi | Number(008,0) | Não | Código do EPI |

---

## Chave Primária

- CodInv
- NumAmb
- DatInv
- CodPRA
- CodGHE
- SeqRis
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R584EPI_005

**Tabela:** R584RIS

| Origem | Destino |
|--------|---------|
| CodInv | CodInv |
| NumAmb | NumAmb |
| DatInv | DatInv |
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| SeqRis | SeqRis |

