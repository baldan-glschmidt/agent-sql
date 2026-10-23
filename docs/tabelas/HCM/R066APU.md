# R066APU

## Descrição

Apuração Colaborador

---

## Resumo

- Campos: 22
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatApu | Date | Não | Data da Apuração |
| HorDat | Number(004,0) | Sim | Código do Horário na Data |
| CodUsu | Number(010,0) | Sim | Código do Usuário da Última Apuração |
| UsuVer | Number(010,0) | Sim | Usuário Verificador |
| DiaAlt | Number(002,0) | Sim | Indica se o Dia foi alterado por Programação/Histórico. |
| CodEsc | Number(009,0) | Sim | Código da Escala |
| CodTma | Number(001,0) | Sim | Código da Turma |
| TurInt | Number(009,0) | Sim | Código da Turma de Intervalo |
| TemExc | String(001) | Sim | Tem Exceção no Dia |
| FalMar | String(001) | Sim | Falta Marcação no Dia |
| OriHor | Number(001,0) | Sim | Origem Horário Apurado |
| ApuJin | String(001) | Sim | Apurado jornada incompleta |
| DatFSo | Date | Sim | Data Final Para Cálculo de Sobreaviso |
| HorFSo | Number(005,0) | Sim | Hora Final Para Cálculo de Sobreaviso |
| ComApu | Date | Sim | Competência |
| PerRef | Date | Sim | Competência do Cálculo |
| FimSep | Date | Sim | Data do Fim da Separação |
| HorSep | Number(005,0) | Sim | Hora do Fim da Separação |
| StaVer | Number(001,0) | Sim | Estado da verificação do dia |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApu

---

## Índices

### R066APUIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- PerRef

---

## Relacionamentos

Nenhum relacionamento cadastrado.
