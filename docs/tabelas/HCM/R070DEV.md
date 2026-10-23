# R070DEV

## Descrição

Devedores de Créditos de Acesso

---

## Resumo

- Campos: 21
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro Colaborador |
| EmpOcr | Number(004,0) | Sim | Código da Empresa Outras Unidades |
| CadOcr | Number(009,0) | Sim | Cadastro do Colaborador de Outra Unidade |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| NumMat | String(015) | Sim | Matrícula do Aluno |
| ProPac | String(020) | Sim | Prontuário do Paciente |
| DatMar | Date | Sim | Data da Marcação |
| HorMar | Number(005,0) | Sim | Hora da Marcação |
| SeqMar | Number(002,0) | Sim | Sequência do Registro |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor no Acesso |
| MotDev | Number(001,0) | Sim | Motivo do Crachá na Lista de Devedores de Créditos de Refeitório |
| TipRes | Number(001,0) | Sim | Tipo do Documento do  Visitante |
| DocRes | String(020) | Sim | Número do Documento do Visitante |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |

---

## Chave Primária

Não possui.

---

## Índices

### R070DEVIndice1

**Tipo:** Não unico

Campos:
- NumCra
- DatMar
- HorMar
- SeqMar

---

## Relacionamentos

Nenhum relacionamento cadastrado.
