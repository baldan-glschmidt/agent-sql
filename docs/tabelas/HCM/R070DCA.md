# R070DCA

## Descrição

Definição de Créditos de Acesso

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodEsc | Number(009,0) | Não | Código da Escala |
| TipPes | Number(001,0) | Não | Tipo de Pessoa que receberá o Crédito |
| IniFai | Number(005,0) | Não | Hora de Início da Faixa de Crédito |
| FimFai | Number(005,0) | Sim | Hora Fim da Faixa de Crédito |
| CreDia | Number(002,0) | Sim | Qtde de Créditos por Dia Segundo a Faixa |
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| LimCon | Number(002,0) | Sim | Limite de consumo diário na faixa |

---

## Chave Primária

- NumEmp
- CodFil
- CodEsc
- TipPes
- VerPlf
- CodPlf
- IniFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070DCA_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

