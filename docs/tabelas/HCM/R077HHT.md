# R077HHT

## Descrição

Histórico Habilidades Técnicas

---

## Resumo

- Campos: 22
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CodHte | String(006) | Não | Código da Habilidade Técnica |
| CmpHab | Date | Não | Competência de Início da Habilidade Técnica |
| TipChb | String(001) | Sim | Certificado (S,N) |
| DatVal | Date | Sim | Data de Validade da Habilidade |
| TipCer | Number(001,0) | Sim | Tipo de Certificador |
| CadCer | Number(009,0) | Sim | Cadastro do Certificador |
| DatCer | Date | Sim | Data da Certificação |
| ObsCer | String(200) | Sim | Observações |
| NotPrf | Number(005,2) | Sim | Nota Média de Performance |
| PerPrf | Number(005,2) | Sim | %  Médio Performance |
| NotDom | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Nota Média de Domínio |
| PerDom | Number(005,2) | Sim | % Conhecimento |
| PerApf | Number(005,2) | Sim | % Aperfeiçoamento |
| PerFor | Number(005,2) | Sim | % Formação |
| OriHHT | String(001) | Sim | Apresenta a origem do Histórico de Habilidade |
| LotCer | Number(009,0) | Sim | Número do lote de Certificação em que foi gerado o Histórico |
| NomArq | String(250) | Sim | Arquivo |
| PtsPos | Number(004,0) | Sim | Total de pontos possíveis |
| PtsCon | Number(006,2) | Sim | Total de pontos conquistados |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodHte
- CmpHab

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077HHT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R077HHT_003

**Tabela:** R077HTE

| Origem | Destino |
|--------|---------|
| CodHte | CodHte |

