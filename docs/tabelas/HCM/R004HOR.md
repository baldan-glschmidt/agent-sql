# R004HOR

## Descrição

Horários

---

## Resumo

- Campos: 29
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHor | Number(004,0) | Não | Código do Horário |
| DesHor | String(030) | Sim | Descrição do Horário |
| TabEst | Number(004,0) | Sim | Define a qual estrutura pertence o Horário |
| TurHor | Number(001,0) | Sim | Turno do Horário |
| JorHor | String(001) | Sim | Tipo de Jornada do Horário |
| SepJor | Number(005,0) | Sim | Separação de Jornada |
| FatRed | Number(005,0) | Sim | Fator de Horas da Jornada |
| LiERef | Number(005,0) | Sim | Limite de Extras na Refeição |
| ToEEnS | Number(005,0) | Sim | Tolerância de Extras Ent/Sai |
| ToERef | Number(005,0) | Sim | Tolerância de Extras na Refeição |
| ToFHor | Number(005,0) | Sim | Tolerância Diária de Faltas |
| ToFEnS | Number(005,0) | Sim | Tolerancia de Faltas Ent/Sai (Horário Tipo Móvel) |
| ToFRef | Number(005,0) | Sim | Tolerancia de Faltas na Refeição (Horário Tipo Móvel) |
| TipHor | Number(001,0) | Sim | Tipo de Horário |
| CRfMov | Number(001,0) | Sim | Tipo do Cálculo da Refeição Móvel |
| HDdPrd | Number(010,0) | Sim | Quantidade de Horas a Deduzir da Produção |
| HorTrb | Number(005,0) | Sim | Horas Trabalhadas Dia |
| CodSin | Number(004,0) | Sim | Código do sindicato |
| HorExt | Number(005,0) | Sim | Horas Extras |
| HorNot | Number(005,0) | Sim | Horas Noturnas |
| ExtAdi | String(001) | Sim | Gerar Adicional de Horas Extras 12 Horas |
| ToEHor | Number(005,0) | Sim | Tolerância Diária de Extras |
| CalFal | Number(001,0) | Sim | Calcular faltas |
| JorAce | Number(001,0) | Sim | Calcula Faixa Horária de Acesso |
| FleEso | String(001) | Sim | Indicar se é permitida a flexibilidade |
| TipInt | Number(001,0) | Sim | Tipo de Intervalo da Jornada |
| CalInt | String(001) | Sim | Calcula o Intervalo Indenizado |
| IniInd | Number(005,0) | Sim | Inicio do Intervalo Indenizado |
| FimInd | Number(005,0) | Sim | Fim do Intervalo Indenizado |

---

## Chave Primária

- CodHor

---

## Índices

### R004HORIndice2

**Tipo:** Não unico

Campos:
- DesHor

---

## Relacionamentos

Nenhum relacionamento cadastrado.
