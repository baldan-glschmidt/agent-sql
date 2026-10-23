# R304ALT

## Descrição

e-Sfinge Online - Alteração da Posse

---

## Resumo

- Campos: 23
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| NumEsp | Number(006,0) | Não | Número da Especialidade |
| NumIns | String(016) | Não | Número da Inscrição |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CarFun | String(016) | Não | Código do cargo ou função atribuído pela unidade |
| DatIni | Date | Não | Data de Início da Vigência do Cargo |
| DatAlt | Date | Não | Data de Alteração |
| SeqReg | Number(009,0) | Não | Sequência |
| TipAlt | Number(002,0) | Não | Tipo de Alteração da Posse |
| DatPos | Date | Sim | Data da Posse |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| PidSta | String(030) | Sim | Pid Status |
| CmpAu1 | Date | Sim | Campo Auxiliar 1 |
| CmpAu2 | Date | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(008,0) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(008,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Number(008,0) | Sim | Campo Auxiliar 5 |
| CmpAu6 | Number(008,0) | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(002) | Sim | Campo Auxiliar 7 |
| CmpAu8 | String(002) | Sim | Campo Auxiliar 8 |
| CmpAu9 | String(2000) | Sim | Campo Auxiliar 9 |

---

## Chave Primária

- NumEmp
- NumEdi
- NumEsp
- NumIns
- TipQua
- CarFun
- DatIni
- DatAlt
- SeqReg

---

## Índices

### R304ALTIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
