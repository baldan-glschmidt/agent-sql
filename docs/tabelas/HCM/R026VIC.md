# R026VIC

## Descrição

Venctos Imposto Fed. Complemen

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
| CodVim | Number(003,0) | Não | Código da Tabela |
| PerApu | Date | Não | Período Apuração |
| IniApu | Date | Não | Dia Início Apuração |
| FimApu | Date | Sim | Dia Fim Apuração |
| DatCor | Date | Sim | Data de Início da Correção |
| DatVen | Date | Sim | Data do Vencimento |

---

## Chave Primária

- CodVim
- PerApu
- IniApu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026VIC_000

**Tabela:** R026VIM

| Origem | Destino |
|--------|---------|
| CodVim | CodVim |

