# R006ESC

## Descrição

Escalas

---

## Resumo

- Campos: 37
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEsc | Number(009,0) | Não | Código da Escala |
| NomEsc | String(030) | Sim | Descrição da Escala |
| TabEst | Number(004,0) | Sim | Define a qual estrutura pertence a Escala |
| ClaEsc | Number(004,0) | Sim | Classe da Escala |
| HorDsr | Number(010,0) | Sim | Horas de DSR |
| HorSem | Number(010,0) | Sim | Horas na Semana |
| HorMes | Number(010,0) | Sim | Horas no Mês |
| LimBa1 | Number(010,0) | Sim | Limite 1 do Banco de Horas |
| LimBa2 | Number(010,0) | Sim | Limite 2 do Banco de Horas |
| TipFer | String(001) | Sim | Tipo de Feriado da Escala |
| TabFer | Number(004,0) | Sim | Código Tabela de Feriados |
| FerOfi | Number(004,0) | Sim | Código Tabela de Feriados |
| MarFol | Number(001,0) | Sim | Considerar Marcações na Folga |
| SepFol | Number(010,0) | Sim | Separação de Jornada na Folga |
| PrjDFo | Number(001,0) | Sim | Projetar Horário em Dias de Folga |
| CodDFa | Number(003,0) | Sim | Código da Tabela de Dias Facultativos |
| TipEsc | String(001) | Sim | Tipo da Escala |
| TipBus | Number(001,0) | Sim | Tipo da Busca Automática |
| TurEsc | Number(001,0) | Sim | Turno da Escala |
| VerInt | String(001) | Sim | Consistência Interjornada |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso para os Dias Normais |
| PrmFer | Number(005,0) | Sim | Permissão de Acesso para os Feriados |
| PrmSab | Number(005,0) | Sim | Permissão de Acesso para os Sábados |
| PrmDom | Number(005,0) | Sim | Permissão de Acesso para os Domingos |
| DesRev | String(030) | Sim | Descrição do tipo de revezamento para emissão do PPP |
| CodHDi | Number(003,0) | Sim | Código das Horas Dispensadas |
| HorTrb | Number(004,0) | Sim | Código do Horário de Trabalho |
| HorFol | Number(004,0) | Sim | Código do Horário de Folga |
| HorDup | Number(004,0) | Sim | Código do Horário de Turno Duplo |
| TraTrb | String(001) | Sim | Tratar Trabalho |
| TipJor | Number(002,0) | Sim | Tipo de jornada para o eSocial |
| TipJoS | Number(002,0) | Sim | Tipo de jornada para o eSocial Simplificado |
| DesJor | String(100) | Sim | Descrição da jornada para o eSocial |
| PagEPF | String(001) | Sim | Pagar extras proporcionais no feriado |
| EscNot | String(001) | Sim | Escala noturna |
| DesSim | String(999) | Sim | Descrição da jornada para o eSocial Simplificado |
| USU_DatExt | Date | Sim | Data de Extins?o |

---

## Chave Primária

- CodEsc

---

## Índices

### R006ESCIndice2

**Tipo:** Não unico

Campos:
- NomEsc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
