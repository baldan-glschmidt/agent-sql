# R017FAP

## Descrição

Faixa de Acesso da Permissão por Posto de Trabalho

---

## Resumo

- Campos: 10
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| IniFai | Number(005,0) | Não | Início da Faixa p/ Marcação de Acesso |
| DiaSem | Number(001,0) | Não | Dia da Semana |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| FimFai | Number(005,0) | Sim | Fim da Faixa p/ Marcação de Acesso |

---

## Chave Primária

- EstPos
- PosTra
- CodPlt
- CodRlg
- VerPlf
- CodPlf
- IniFai
- DiaSem
- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017FAP_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

